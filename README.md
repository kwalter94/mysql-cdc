# MaxwellD MySQL CDC

A setup for Change Data Capture from MySQL to Kafka using MySQL binary
log parser, [Maxwell Daemon](https://maxwells-daemon.io).

## How to run

1. Have docker and docker-compose installed
2. Start application as follows:

    ```sh
    docker-compose up
    ```

3. Attach to log file where CDC events are being written (there is
   a shell script running that's creating entries in MySQL. These
   entries are being captured by Maxwell's Daemon from the binary
   log and written to Kafka. From there they are being consumed
   by a python script and written to a log file)

    ```sh
    tail -f cdc-processor/log/cdc.log
    ```
