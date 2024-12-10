use std::time::{Duration, Instant};

fn main() {

    let mut iterator: f64 = 0.0;
    let mut approximation_squared: f64 = 0.0;
    let mut approximation: f64;
    let mut previous_approximation: f64 = 0.0;
    let mut deviation: f64;
    let mut final_accuracy: u8 = 0;
    let mut start_time: Instant;
    let mut iteration_time: Duration;
    let mut total_computation_time: Duration = Duration::from_secs(0); // Duration::from_secs(0) is just a temporary value in order to initialize the total_computation_time variable.

    loop {

        start_time = Instant::now();
        approximation_squared += (f64::powf(-1.0, iterator) / (iterator + 1.0)) * inner_summation_loop(iterator as u16);
        approximation = f64::powf(approximation_squared, 0.5) * 4.0;
        iteration_time = start_time.elapsed();

        println!("Iteration {}", iterator as u16 + 1);
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

        println!("Iteration duration: {:?}", end_time - start_time);
        total_computation_time += end_time - start_time;
    
        deviation = approximation - previous_approximation;
        if deviation.abs() < 1e-50 {
            println!("\nSummation converged. Terminating program...");
            break;
        }
        else { println!("Deviation from previous iteration: {:.51}\n", deviation) }

        previous_approximation = approximation;
        iterator += 1.0;

    }

    println!("Computed {} correct decimal places in {:?} and {} iterations.", final_accuracy, total_computation_time, iterator as u16 + 1);
}

fn inner_summation_loop (num: u16) -> f64 {
    let mut result: f64 = 0.0;

    for i in 0 .. num + 1 {
        result += 1.0 / (2.0 * (i as f64) + 1.0)
    }

    return result
}