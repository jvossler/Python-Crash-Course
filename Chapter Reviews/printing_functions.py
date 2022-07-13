def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()

        # Simulate creating a 3D print from the design.
        print("Printing model: " + current_design)
        completed_models.append(current_design)

    # # Start with some designs that need to be printed. Think of a few, 
    # # then write them out in your own words.
    # unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
    # completed_models = []
    # # Simulate printing each design, until none are left.
    # #  Move each design to completed_models after printing.
    # while unprinted_designs:
    #     current_design = unprinted_designs.pop()
    #     print(f"Printing model: {current_design}")
    #     completed_models.append(current_design)
        
    # # Display all completed models.
    # print("\nThe following models have been printed:")
    # for completed_model in completed_models:
    #     print(completed_model)

