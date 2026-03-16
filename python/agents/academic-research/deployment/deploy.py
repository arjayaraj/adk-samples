import os

import vertexai
from absl import app, flags
from academic_research.agent import root_agent
from dotenv import load_dotenv
from vertexai import agent_engines
from vertexai.preview.reasoning_engines import AdkApp

FLAGS = flags.FLAGS
flags.DEFINE_string("project_id", None, "GCP project ID.")
flags.DEFINE_string("location", None, "GCP location.")
flags.DEFINE_string("bucket", None, "GCP bucket.")
flags.DEFINE_string("resource_id", None, "ReasoningEngine resource ID.")

flags.DEFINE_bool("list", False, "List all agents.")
flags.DEFINE_bool("create", False, "Creates a new agent.")
flags.DEFINE_bool("delete", False, "Deletes an existing agent.")
flags.mark_bool_flags_as_mutual_exclusive(["create", "delete"])

def session_service_builder():
  """Builds the session service to use in the ADK app."""

  # This is needed to ensure InitGoogle and AdkApp setup is called first.
  from google.adk.sessions.in_memory_session_service import InMemorySessionService

  # if "GOOGLE_CLOUD_AGENT_ENGINE_ID" not in os.environ:
  return InMemorySessionService()

adk_app = AdkApp(
    agent=root_agent,
    enable_tracing=True,
    session_service_builder=session_service_builder,
)
