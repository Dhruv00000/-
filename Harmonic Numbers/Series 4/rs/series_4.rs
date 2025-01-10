use std::time::{Duration, Instant};

fn main() {

    let mut iterator: u32 = 1;
    let mut nth_harmonic: f64 = 0.0;
    let mut approximation_exponentiated: f64 = 0.0;
    let mut approximation: f64;
    let mut previous_approximation: f64 = 0.0;
    let mut deviation: f64;
    let mut final_accuracy: u8 = 0;
    let mut start_time: Instant;
    let mut iteration_time: Duration;
    let mut total_computation_time: Duration = Duration::from_secs(0); // Duration::from_secs(0) is just a temporary value in order to initialize the total_computation_time variable.

    loop {

        start_time = Instant::now();

        nth_harmonic += 1.0 / iterator as f64;
        approximation_exponentiated += 72.0 * nth_harmonic / u32::pow(iterator, 3) as f64;
        approximation = f64::powf(approximation_exponentiated, 1.0/4.0);

        iteration_time = start_time.elapsed(); // only the mathematical computations are considered in the total computation time, and everything else like calculating the deviation and accuracy is not considered.

        println!("Iteration {}", iterator);
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
        else { println!("Deviation from previous iteration: {:.51}\n", deviation) }

        println!("Iteration duration: {:?}\n", iteration_time);
        total_computation_time += iteration_time;

        previous_approximation = approximation;
        iterator += 1;

    }

    println!("Computed {} correct decimal places in {:?} and {} iterations.\n", final_accuracy, total_computation_time, iterator);
}