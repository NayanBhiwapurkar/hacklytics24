from core.innSight import InnSight

inn_sight = InnSight()
res_1 = inn_sight.answer_user_prompt("Suggest me the best hotel in Istanbul?")
print(res_1)

res_2 = inn_sight.answer_user_prompt("Tell me more about it?")
print(res_2)