# MyWatch
MyWatch is tool which watches a directory for changes and runs a command everytime, a change happens.

## Usage
./mywatch.py <directory> <command>

## Example
./mywatch.py src/ 'make build'

Evertime you save a file in the src directory, the build make target will be triggered.
