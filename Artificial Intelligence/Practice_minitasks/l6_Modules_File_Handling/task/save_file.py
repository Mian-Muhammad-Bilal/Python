def save_results_to_file(results, output_file):
    try:
        with open(output_file, 'w') as file:
            file.write(str(results))
            print(f"Results saved to {output_file}")
    except IOError as e:
        print(f"Error: {e}")
