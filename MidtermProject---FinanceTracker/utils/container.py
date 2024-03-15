import punq as punq

from accounts.dependencies import AccountCreateDependency
from transactions.dependencies import TransactionCreateDependency
from utils.repository import AbcRepository
from utils.dependencies import GetListDependency, RetrieveDependency, DeleteDependency
from users.dependencies import UserCreateDependency
from budgets.dependencies import BudgetCreateDependency
from categories.dependencies import CategoryCreateDependency
from expenses.dependencies import ExpenseCreateDependency


def get_container(repository: type[AbcRepository]) -> punq.Container:
    container = punq.Container()

    container.register(AbcRepository, repository, instance=repository())

    container.register(GetListDependency)
    container.register(RetrieveDependency)
    container.register(DeleteDependency)

    container.register(UserCreateDependency)

    container.register(AccountCreateDependency)

    container.register(TransactionCreateDependency)

    container.register(CategoryCreateDependency)

    container.register(BudgetCreateDependency)

    container.register(ExpenseCreateDependency)

    return container
