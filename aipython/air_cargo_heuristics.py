def h_movement_cost(state, goal):
    """ Based on number of actions """
    movement_cost = 0
    
    for fact in goal:
        #if cargo (object) which should be at the particular airport is not there
        if goal[fact] is True and state.get(fact, False) is False and '_at_' in fact:
            cargo, dest = fact.split("_at_")
            if cargo.startswith("c"): 
                current_loc = next((key.split('_at_')[1] for key, loc in state.items() if cargo in key and loc and '_at_' in key), None)
                
                #cargo is at the correct airport 
                if current_loc == dest:
                    continue
                
                #cargo is at the wrong airport
                if current_loc:
                    #is there any airport at the airport where parcel is located
                    planes_on_wrong_airport = [key.split("_at_")[0] for key, loc in state.items() if "p" in key and loc and "_at_" in key and key.split("_at_")[1] == current_loc]
                    
                    if planes_on_wrong_airport:
                        #you have to load it, fly and unload
                        movement_cost += 3
                    
                    # there is no plane at the airport where parcel is placed
                    else:
                        movement_cost += 4
                else:
                    # cargo is not at any airport, check if it is in a plane
                    current_plane = next((key.split('_in_')[1] for key, loc in state.items() if cargo in key and loc and '_in_' in key), None)
                    
                    if current_plane:
                        # the plane's location
                        plane_location = next((key.split('_at_')[1] for key, loc in state.items() if current_plane in key and loc and '_at_' in key), None)
                        
                        if plane_location == dest:
                            # Cargo is in the plane, which is at the correct airport so just unload 
                            movement_cost += 1 
                        else:
                            # plane is not at the correct destination, so cost for flight and unload
                            movement_cost += 2
                
    return movement_cost