from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional, Callable

class AgentsInterface(ABC):
    """
    CoreX Interface for Agents.

    This interface standardizes operations for managing agentic AI workflows. It is inspired by the
    OpenAI Agents SDK and includes primitives for agent registration, configuration, messaging,
    tool integration, guardrails, handoffs, tracing, and monitoring. Implementations should provide
    mechanisms for running an agent loop that processes user inputs, calls tools, handles handoffs,
    and produces a final output.
    """

    # Registration and lifecycle management
    @abstractmethod
    def register_agent(self, agent_id: str, config: Optional[Dict[str, Any]] = None) -> None:
        """
        Register a new agent with the system.

        :param agent_id: Unique identifier for the agent.
        :param config: Optional configuration for the agent.
        """
        raise NotImplementedError("register_agent must be implemented by subclasses.")

    @abstractmethod
    def deregister_agent(self, agent_id: str) -> None:
        """
        Deregister an agent from the system.

        :param agent_id: Unique identifier for the agent.
        """
        raise NotImplementedError("deregister_agent must be implemented by subclasses.")

    @abstractmethod
    def start_agent(self, agent_id: str) -> None:
        """
        Start a registered agent.

        :param agent_id: Unique identifier for the agent.
        """
        raise NotImplementedError("start_agent must be implemented by subclasses.")

    @abstractmethod
    def stop_agent(self, agent_id: str) -> None:
        """
        Stop a running agent.

        :param agent_id: Unique identifier for the agent.
        """
        raise NotImplementedError("stop_agent must be implemented by subclasses.")

    @abstractmethod
    def update_agent_config(self, agent_id: str, new_config: Dict[str, Any]) -> None:
        """
        Update the configuration of a specific agent.

        :param agent_id: Unique identifier for the agent.
        :param new_config: Dictionary containing new configuration parameters.
        """
        raise NotImplementedError("update_agent_config must be implemented by subclasses.")

    # Messaging and conversation management
    @abstractmethod
    def add_message(self, message: str, role: str = "user") -> None:
        """
        Add a message to the agent's conversation history.

        :param message: The message content.
        :param role: The role of the message sender (e.g., 'user', 'assistant').
        """
        raise NotImplementedError("add_message must be implemented by subclasses.")

    @abstractmethod
    def get_last_message(self) -> str:
        """
        Retrieve the last message from the agent's conversation.

        :return: The last message as a string.
        """
        raise NotImplementedError("get_last_message must be implemented by subclasses.")

    @abstractmethod
    def run_loop(self, initial_message: str) -> Any:
        """
        Run the agent loop until final output is produced. The loop should handle calling tools,
        validating outputs via guardrails, processing handoffs, and tracing the execution.

        :param initial_message: The initial user message to start the conversation.
        :return: The final output produced by the agent.
        """
        raise NotImplementedError("run_loop must be implemented by subclasses.")

    # Tool and guardrail integration
    @abstractmethod
    def add_tool(self, tool: Callable[..., Any]) -> None:
        """
        Add a tool (function) that the agent can call to perform specific tasks.

        :param tool: A callable representing the tool.
        """
        raise NotImplementedError("add_tool must be implemented by subclasses.")

    @abstractmethod
    def add_guardrail(self, guardrail: Callable[[Any], bool]) -> None:
        """
        Add a guardrail check that validates inputs or outputs of the agent.

        :param guardrail: A callable that takes an agent output and returns True if valid.
        """
        raise NotImplementedError("add_guardrail must be implemented by subclasses.")

    @abstractmethod
    def set_instructions(self, instructions: str) -> None:
        """
        Set or update the agent's instructions, which guide its behavior and responses.

        :param instructions: A string containing the agent's instructions.
        """
        raise NotImplementedError("set_instructions must be implemented by subclasses.")

    # Handoff and multi-agent coordination
    @abstractmethod
    def handoff(self, target_agent: "AgentsInterface") -> None:
        """
        Delegate control to another agent via a handoff.

        :param target_agent: The agent to which control should be transferred.
        """
        raise NotImplementedError("handoff must be implemented by subclasses.")

    # Tracing and debugging
    @abstractmethod
    def get_trace(self) -> Dict[str, Any]:
        """
        Retrieve tracing information for the agent's execution. This information can be used
        to visualize the flow, debug issues, and optimize performance.

        :return: A dictionary containing trace data.
        """
        raise NotImplementedError("get_trace must be implemented by subclasses.")

    # Monitoring and activity logging
    @abstractmethod
    def monitor(self, callback: Callable[[str, str], None]) -> None:
        """
        Monitor agent events and status changes, invoking the callback with the agent ID and new status.

        :param callback: A callable that accepts two parameters: agent_id and new_status.
        """
        raise NotImplementedError("monitor must be implemented by subclasses.")

    @abstractmethod
    def heartbeat(self, agent_id: str) -> bool:
        """
        Check the responsiveness of the specified agent.

        :param agent_id: Unique identifier for the agent.
        :return: True if the agent responds to the heartbeat signal, False otherwise.
        """
        raise NotImplementedError("heartbeat must be implemented by subclasses.")

    @abstractmethod
    def schedule_task(self, agent_id: str, task_name: str, schedule: str, payload: Optional[Dict[str, Any]] = None) -> None:
        """
        Schedule a recurring task for the agent.

        :param agent_id: Unique identifier for the agent.
        :param task_name: Name of the task to schedule.
        :param schedule: Schedule definition (e.g., a cron expression).
        :param payload: Optional data to pass to the task.
        """
        raise NotImplementedError("schedule_task must be implemented by subclasses.")

    @abstractmethod
    def get_agent_metrics(self, agent_id: str) -> Dict[str, Any]:
        """
        Retrieve performance or operational metrics for the specified agent.

        :param agent_id: Unique identifier for the agent.
        :return: A dictionary of metric names and their corresponding values.
        """
        raise NotImplementedError("get_agent_metrics must be implemented by subclasses.")

    @abstractmethod
    def log_activity(self, agent_id: str, activity: str, details: Optional[Dict[str, Any]] = None) -> None:
        """
        Log an activity or event related to the agent's operation.

        :param agent_id: Unique identifier for the agent.
        :param activity: A description of the activity or event.
        :param details: Optional additional details regarding the activity.
        """
        raise NotImplementedError("log_activity must be implemented by subclasses.")

    @abstractmethod
    def recover(self, agent_id: str) -> None:
        """
        Attempt to recover the agent from a failure or unexpected state.

        :param agent_id: Unique identifier for the agent.
        """
        raise NotImplementedError("recover must be implemented by subclasses.")

    @abstractmethod
    def shutdown_all(self) -> None:
        """
        Shutdown all registered agents gracefully.
        """
        raise NotImplementedError("shutdown_all must be implemented by subclasses.")
