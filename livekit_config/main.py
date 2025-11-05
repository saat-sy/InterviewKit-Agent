from dotenv import load_dotenv

from livekit import agents
from uuid import uuid4, uuid5, UUID
from livekit.agents import AgentSession, Agent, RoomInputOptions
from livekit.plugins import (
    cartesia,
    deepgram,
    noise_cancellation,
    silero,
)
from livekit.plugins.turn_detector.multilingual import MultilingualModel
from livekit_config.langgraph_livekit_agents import LangGraphAdapter
from langgraph.pregel.remote import RemoteGraph
from livekit_config.constants import Constants

load_dotenv()

def get_thread_id(sid: str | None) -> str:
    NAMESPACE = UUID("41010b5d-5447-4df5-baf2-97d69f2e9d06")
    if sid is not None:
        return str(uuid5(NAMESPACE, sid))
    return str(uuid4())

class Assistant(Agent):
    def __init__(self) -> None:
        super().__init__(instructions="You are a helpful voice AI assistant.")


async def entrypoint(ctx: agents.JobContext):
    await ctx.connect()

    participant = await ctx.wait_for_participant()
    thread_id = get_thread_id(participant.sid)
    
    graph = RemoteGraph("agent", url="http://localhost:2024")

    session = AgentSession(
        stt=deepgram.STT(model="nova-3", language="multi"),
        llm=LangGraphAdapter(
            graph,
            config={"configurable": {"thread_id": thread_id}},
            initial_information={
                "raw_resume": Constants.RAW_RESUME,
                "raw_job_description": Constants.RAW_JOB_DESCRIPTION,
                "duration": "10",
            }
        ),
        tts=cartesia.TTS(),
        vad=silero.VAD.load(),
        turn_detection=MultilingualModel(),
    )

    await session.start(
        room=ctx.room,
        agent=Assistant(),
        room_input_options=RoomInputOptions(
            noise_cancellation=noise_cancellation.BVC(),
        ),
    )

    await session.generate_reply(
        instructions="Greet the user and offer your assistance."
    )


if __name__ == "__main__":
    agents.cli.run_app(agents.WorkerOptions(entrypoint_fnc=entrypoint))
    