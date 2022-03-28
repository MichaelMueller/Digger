while($true) {
    echo "Starting Proxy"
    ssh <host> -R 23000:localhost:2276 -N
    echo "Connection Error"
    echo "Sleeping 1s"
    Start-Sleep -Seconds 1
}