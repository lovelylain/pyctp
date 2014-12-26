package  main

import "time"
import "fmt"

func main(){
    var tcur = time.Now()
    var z = 0
    for {
        z += 2
        if z > 999999999{
            break
        }
    }
    var tafter = time.Now()
    var td = tafter.Sub(tcur)
    fmt.Println("耗时:",td,z)
    
}
