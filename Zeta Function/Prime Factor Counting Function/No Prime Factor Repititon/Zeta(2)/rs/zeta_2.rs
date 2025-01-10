use std::time::{Duration, Instant};

fn main() {

    let mut iteration_counter: u16 = 1;
    let mut n: u16 = 2;
    let mut approximation_squared_inverted: f64 = 0.0;
    let mut approximation: f64;
    let mut previous_approximation: f64 = 0.0;
    let mut deviation: f64;
    let mut final_accuracy: u8 = 0;
    let mut start_time: Instant;
    let mut iteration_time: Duration;
    let mut total_computation_time: Duration = Duration::from_secs(0); // Duration::from_secs(0) is just a temporary value in order to initialize the total_computation_time variable.

    loop {

        if epsilon_modified(n) % 2 != 0 {
            start_time = Instant::now();
            approximation_squared_inverted += 2.0 / (9.0 * f64::powf(n as f64, 2.0));
            approximation = f64::powf(approximation_squared_inverted, -1.0/2.0);
            iteration_time = start_time.elapsed(); // only the mathematical computations are considered in the total computation time, and everything else like calculating the deviation and accuracy is not considered.

            println!("Iteration {}", iteration_counter);
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
            if deviation.abs() < 1e-50 {
                println!("\nSummation converged. Terminating program...");
                break;
            }
            else { println!("Deviation from previous iteration: {:.51}\n", deviation); }

            println!("Iteration duration: {:?}\n", iteration_time);
            total_computation_time += iteration_time;

            previous_approximation = approximation;
            iteration_counter += 1;
        }

        n += 1;
    }

    println!("Computed {} correct decimal places in {:?} and {} iterations.\n", final_accuracy, total_computation_time, iteration_counter);
}

fn epsilon_modified(mut num: u16) -> u16 {
    let mut prime_factor_count: u16 = 0;

    if num % 2 == 0 {
        num /= 2;
        prime_factor_count += 1;
    }

    let mut i: u16 = 3;
    while i <= num {
        if num % i == 0 {
            num /= i;
            prime_factor_count += 1;
        }
        if num % i == 0 {  prime_factor_count = 0; } // These two lines ensure that no prime factor is repeated.

        i += 2;
    }

    if num % 2 == 0 { prime_factor_count = 0; }

    return prime_factor_count;

}