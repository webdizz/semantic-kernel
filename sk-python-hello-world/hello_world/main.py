import semantic_kernel as sk
from semantic_kernel.connectors.ai.open_ai import (
    OpenAITextCompletion,
)
from semantic_kernel.orchestration.context_variables import ContextVariables


def main():
    kernel = sk.Kernel()

    api_key, org_id = sk.openai_settings_from_dot_env()

    kernel.add_text_completion_service(
        "dv", OpenAITextCompletion("text-davinci-003", api_key, org_id)
    )
    skills_directory = "skills"
    code_skill = kernel.import_semantic_skill_from_directory(
        skills_directory, "CodeSkill"
    )

    python_function = code_skill["Python"]

    python_code(python_function, "how to get current date and time with custom format?")


def python_code(python_function, task: str):
    result = python_function(task)
    print(result)


if __name__ == "__main__":
    main()
