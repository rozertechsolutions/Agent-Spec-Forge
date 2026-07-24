# AI Specialized Departments

AI Specialized Departments is a repository for creating professional AI configurations adapted to specific departments and specialties.

The objective is to define what an AI environment needs in order to work effectively in a professional area and then prepare the corresponding configuration for each supported platform.

The project separates the professional definition of a department from the way each platform implements it. This allows the same department to be adapted to different AI tools without redefining its purpose, roles, capabilities, procedures, instructions, integrations, or operational requirements from scratch.

## Project Structure

```text
ai-specialized-departments/
├── departments/
├── shared/
├── platform/
└── README.md
```

### `departments/`

Contains the professional definition of each department and its specialties.

Each department may define the roles, capabilities, procedures, instructions, MCP requirements, events, and other elements needed for that area of work.

### `shared/`

Contains reusable components that can be used by more than one department, such as common roles, capabilities, procedures, instructions, MCP definitions, or external integrations.

### `platform/`

Contains the real implementation of each department for the supported AI platforms.

Each platform keeps its own native configuration structure, formats, files, terminology, and capabilities.

## Goal

The final result should allow a user to choose a professional department and obtain a practical AI configuration for the platform they use.

The repository is intended to support different types of AI environments, including IDE-based tools, CLI agents, desktop applications, web platforms, and other configurable AI systems when appropriate.

The list of departments, specialties, and supported platforms will evolve as the project is developed.


## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
