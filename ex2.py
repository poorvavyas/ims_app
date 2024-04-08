# Person(FName,LName,SpouseName,DOB,Gender,FatherName,MotherName,Aadhar)
#
#     Let’s say “Client_1” wants to apply restrictions as
#
#         Male(FName,LName,SpouseName)
#
#         Female(FName,LName,FatherName,MotherName)
#
#     and “Client_2” would like their restrictions as
#
#         Male(FName,LName)
#
#         Female(FName,LName,DOB)
#
#     Design and Implement a dynamic pattern to support multiple clients accessibility on Person entity.


#  Table Name: Client_constraints
# Client_id
# based_on (Gender : M, F)
# required Field (all required field)

# class api_view():
# check request.client information
# fetch client detail from constraint table
# perform validation if not valid return 404 else post data and perform further operation



#  Given a robot, allow it to rotate multiple times to multiple directions (N,S,E,W) based on following inputs
#
#         Direction - It could be Clockwise(C) or AntiClockwise(A)
#
#         Turns - Turns could vary from 0 to MAX_INT allowed
#
#     After each input, you should be able to identify the robot direction and allow it to rotate further
#
#     Always consider N(north) as your starting direction to begin with.
#
# Inputs:
#
#     Given input as N → (C, 2) → (1?) → (A,3) → (2?) → (C,1) → (3?) → (A, 104567) → ?? → (C, 9933) → ???
#
#         1? = S, 2? = W, 3? = N, ?? = (find_out), ??? = (find_out)

# ashwani.kumar@protium.co.in

input_data = [('C', 2), ('A',3), ('C',1), ('A', 104567), ('C', 9933)]
direction_dict = {0: 'N', 1: 'E', 2: 'S', 3: 'W'}


def rotation():
    res = []
    last_rotation = 0
    for i in range(len(input_data)):
        if input_data[i][0] == 'A':
            anti_val = input_data[i][1] % 4
            curr_val = last_rotation + (4-anti_val)
        else:
            curr_val = (input_data[i][1] + last_rotation) % 4
        curr_val = curr_val % 4
        last_rotation = curr_val
        res.append(direction_dict[curr_val])
    return res


print(rotation())
