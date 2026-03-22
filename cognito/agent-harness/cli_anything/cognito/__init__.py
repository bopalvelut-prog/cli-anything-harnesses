import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def forms(): click.echo('Cognito Forms forms')
@cli.command()
def entries(): click.echo('Cognito Forms entries')
if __name__ == '__main__': cli()
