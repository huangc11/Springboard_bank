import datetime as dt
from utility import Utility as ut
from database import Database

from customer import Customer
from bankaccount import BankAccount, SavingsAccount, CheckingAccount
from customer_account import CustomerAccount
from employee import Employee
from card_application import  CardApplication
from creditcard import CreditCard


class CreditCardManager:
    logger = ut.setup_logger('log_creditcard', 'logs\log_creditcard_manager.log')

    @classmethod
    def log_show_info(cls, message):
        cls.logger.info(message)
        ut.print_info(message)

    @classmethod
    def log_show_error(cls, message):
        cls.logger.info(message)
        ut.print_error(message)

    @classmethod
    def log_show_success(cls, message):
        cls.logger.info(message)
        ut.print_success(message)

    @classmethod
    def get_total_savings_by_customer_id(cls, p_customer_id=169):
        session = Database.get_session()

        queryResult = session.query(
            Customer, BankAccount, CustomerAccount,
        ).filter(
            CustomerAccount.customer_id == Customer.id,
        ).filter(
            CustomerAccount.account_id == BankAccount.account_id,
        ).filter(
            Customer.id == p_customer_id,
        ).all()

        # if return list is empty
        if len(queryResult)==0:
            return 0

        sum = 0
        for q in queryResult:
            if ("sav" in q.BankAccount.account_type):
                sum += q.BankAccount.balance

        #print('sum={}'.format(sum))
        return sum

    @classmethod
    def approve_application(cls):
        """
          Process credicard applcation in table card_application.
          If customer's total savings <less  2000, application will be rejected.
          Otherwise it will approved. A new credit card will be generated and assgined to the applicant
        """

        cls.log_show_info("Requested to approve credit card applications")
        session = Database.get_session()

        t_emp_id = 1

        queryResult = session.query(
            CardApplication). \
            filter(CardApplication.status == 'new') \
            .all()

        for appl in queryResult:
            bal = CreditCardManager.get_total_savings_by_customer_id(appl.customer_id)

            appl.employee_id = t_emp_id
            appl.apprv_date = dt.datetime.today()

            if bal < 2000:
                # total savings <less  2000, application will be rejected
                appl.status = 'rejected'
                appl.note = 'Rejected due to total savings<2000'
                # 'rejected'
                appl.update_at_db({'status': appl.status})


            else:
                # total savings >= 2000, application will be approved and a credit card will be created and assgined to this customer
                appl.status = 'approved'
                t_customer = Customer.get_by_id(appl.customer_id)
                t_cardholder_name = t_customer.name
                new_card = CreditCard.generate_a_new_card(customer_id=appl.customer_id,
                                                          cardholder_name=t_cardholder_name, employee_id=t_emp_id)
                appl.card_id = new_card.id
                appl.update_at_db({'status': appl.status})

        cls.log_show_info('Process completed.')

    @staticmethod
    def menu():




''''
select
c.id, a. *
from ass_customer_account ca, customer

c, bankaccount
a
where
ca.customer_id = c.id
and ca.account_id = a.id
'''

if __name__ =="__main__":
    CreditCardManager.approve_application()