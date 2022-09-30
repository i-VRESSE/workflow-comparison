def restrict_academic(context, tool):
    user = context.trans.user
    if tool.name == 'haddock3academic':
        for user_role in user.roles:
            if user_role.name == 'ACADEMICS':
                return True
        return False
    return True