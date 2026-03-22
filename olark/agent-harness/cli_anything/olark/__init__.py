import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def chats(): click.echo('Olark chats')
@cli.command()
def operators(): click.echo('Olark operators')
if __name__ == '__main__': cli()
