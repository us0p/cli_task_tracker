# Task Tracker
Track and manage your tasks in the CLI.

## Requirements
- [x] Add Task.
- [x] Update Task.
- [x] Delete Task.
- [x] Mark a task as in progress or done.
- [x] List all tasks.
- [x] List all tasks that are done.
- [x] List all tasks that are not done.
- [x] List all tasks that are in progress.
- [ ] Add tests
- [ ] Client should receive only important information, remove "createdAt" and "updatedAt" from response

## Constraints
- Use positional arguments in command line to accept user inputs.
- Use a JSON file to store the tasks in the current directory.
- The JSON file should be created if doesn't exist.
- Use the native file system module to interact with the JSON file.
- Do not use any external libraries or frameworks to build this project.
- Handle errors and edge cases gracefully.

## Task Properties
Each task should have the following properties
- id: unique identifier
- description?: string
- status ['todo' | 'in-progress' | 'done']: 'todo'
- createdAt: date
- updatedAt: date

## Architecture
### Entities
**Task**  
Expects status as input, description is optional. Other fields are provded on creation.

**Methods**:  
- validate() -> Raises EntityValidationError if invalid status.

### Repositories
- TaskRepository: Read/Writes to JSON files. Receive and return Task objects.

### Use cases
- Create Task
    - can't create external fields
- Update Task
    - can't update id
    - can't add external fields
- Delete Task
- List Tasks
    - filter by status

### DTOs
- TaskCLIDTO: Provides formatting for CLI output.

### Controllers
- TaskController: Provides interaction between use cases, repository and DTOs.

### External interfaces
- CLI: binds Controllers to user inputs.
- TaskRepository: Implementation uses fs module to handle JSON files.
