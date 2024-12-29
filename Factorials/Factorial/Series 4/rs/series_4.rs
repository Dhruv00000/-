use std::time::{Duration, Instant};

fn main() {

    let mut iterator: u16 = 0;
    let mut approximation_inverted: f64 = 0.0;
    let mut approximation: f64;
    let mut previous_approximation: f64 = 0.0;
    let mut deviation: f64;
    let mut final_accuracy: u8 = 0;
    let mut start_time: Instant;
    let mut iteration_time: Duration;
    let mut total_computation_time: Duration = Duration::from_secs(0); // Duration::from_secs(0) is just a temporary value in order to initialize the total_computation_time variable.

    loop {

        start_time = Instant::now();
        approximation_inverted += i16::pow(-1, iterator as u32) as f64 * (factorial(4*iterator) * (260 * iterator + 23) as u128) as f64 / (u128::pow(factorial(iterator), 4) * u128::pow(4, 4*iterator as u32) * u128::pow(18, 2*iterator as u32)) as f64;
        approximation = 72.0 / approximation_inverted;
        iteration_time = start_time.elapsed(); // only the mathematical computations are considered in the total computation time, and everything else like calculating the deviation and accuracy is not considered.

        println!("Iteration {}", iterator + 1);
        println!("Approximation = {:.51}", approximation);

        let mut i: u8 = 0;
        for c in String::from("3.141592653589793238462643383279502884197169399375105").chars() {
            if c != match approximation.to_string().chars().nth(i as usize) {
                Some(c2) => c2,
                None => char::from(0)
            } {
                if i < 2 { println!("No accurate decimal places.") }
                else {
                    println!("{} correct decimal place(s)", i - 2);
                    final_accuracy = i - 2;
                }
                break;
            }

            i += 1;
        }

        deviation = approximation - previous_approximation;
        println!("Deviation from previous iteration: {:.51}\n", deviation);

        println!("Iteration duration: {:?}\n", iteration_time);
        total_computation_time += iteration_time;

        if iterator == 5 {
            println!("\nFactorials after this iteration will become too big to store. Terminating the program...");
            break;
        }

        previous_approximation = approximation;
        iterator += 1;

    }

    println!("Computed {} correct decimal places in {:?} and {} iterations.\n", final_accuracy, total_computation_time, iterator + 1);
}

fn factorial(num: u16) -> u128 {
    if num == 0 { return 1; }
    return num as u128 * factorial(num - 1);
}