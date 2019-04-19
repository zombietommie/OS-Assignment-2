/**
 * Tommy Tran
 * 2420005
 * CSCI 4401 - OS
 * Assignment 2 - Question 2
 */

// Imports
import java.util.concurrent.ForkJoinPool;
import java.util.concurrent.ForkJoinTask;
import java.util.concurrent.Semaphore;
import java.util.Random;

enum PhilosopherState {Hungry, Eat, Think}

public class DinePhilo {

    static Semaphore mutex = new Semaphore(1);

    public static void main(String[] args) {

        String[] person = {"P0", "P1", "P2", "P3"};

        PhilosopherState state = PhilosopherState.Eat;
        System.out.println(state);

        int val = new Random().nextInt(32);
        System.out.println(val);

        Thread fork = new Thread(() -> {

            try {
                for (int i = 0; i < 9; i++) {
                    if (mutex.availablePermits() == 1){
                        System.err.println("mutex is available");
                        mutex.acquire();
                    } else if (mutex.availablePermits() == 0) {
                        System.out.println("mutex is not available");
                        mutex.release();
                    }
                }
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        });
        fork.start();
    }
}