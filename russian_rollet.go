package main

import (
	"fmt"
	"math/rand/v2"
	"os/exec"
	"runtime"

	// "syscall"
	"time"
)

var s2 = rand.NewPCG(1, 6)
var r2 = rand.New(s2)

var numeracao_tambor = []int{1, 2, 3, 4, 5, 6}
var tambor_com_bala = rand.IntN(7)

func execute_linux() {
	fmt.Print("POOOOOOOOOOOOOOOOOWWWWWWW!!!!!!!!!!")
	time.Sleep(2 * time.Second)
	// syscall.Reboot(syscall.LINUX_REBOOT_CMD_RESTART)
	// n funciona no windows.
}

func execute_windows() {
	fmt.Print("POOOOOOOOOOOOOOOOOWWWWWWW!!!!!!!!!!")
	time.Sleep(2 * time.Second)
	if err := exec.Command("cmd", "/C", "shutdown", "/r", "/t", "4").Run(); err != nil {
		fmt.Println("Failed to initiate shutdown:", err)
	}
}

func execute() {
	var i string
	if tambor_com_bala == 0 {
		tambor_com_bala = 1
	}
	for _, value := range numeracao_tambor {
		fmt.Print("Deseja atirar? [s/n] ")
		fmt.Scan(&i)
		if i == "s" {
			if tambor_com_bala == value {
				if runtime.GOOS == "windows" {
					execute_windows()
					break
				} else {
					execute_linux()
					break
				}
			}
		} else {
			break
		}
	}
}

func main() {
	execute()
}
