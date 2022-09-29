def restrict_acadamic(context, tool):
    user = context.trans.user
    if tool.name == 'haddock3':
        for user_role in user.roles:
            if user_role.name == 'acadamics':
                return True
        return False
    return True