import chainlit as cl
from src.crew import AutoResearchCrew


@cl.on_chat_start
async def on_chat_start():
    """
    This function runs when the user starts a new session.
    """
    await cl.Message(
        content="👋 **Welcome to AutoResearch Crew!**\n\n"
        "I am a multi-agent system powered by CrewAI & Groq.\n"
        "Give me a topic, and my team (Researcher & Writer) will generate a full report for you."
    ).send()


@cl.on_message
async def main(message: cl.Message):
    """
    This function runs every time the user sends a message.
    """
    topic = message.content

    # Notify user that work has started
    msg = cl.Message(
        content=f"🚀 **Starting research on:** *{topic}*...\n\n_This may take a minute while agents browse the web._"
    )
    await msg.send()

    try:
        # Initialize Crew
        crew = AutoResearchCrew()

        # Run Crew (This is blocking, so the UI waits)
        # In a real heavy-load production, we would use async/threads,
        # but for a demo, this is perfect.
        result = crew.run(topic)

        # Send the final result
        await cl.Message(content=f"## Research Report:\n\n{result}").send()

        # Update status
        msg.content = f"**Research completed for:** *{topic}*"
        await msg.update()

    except Exception as e:
        await cl.Message(content=f"An error occurred: {str(e)}").send()
