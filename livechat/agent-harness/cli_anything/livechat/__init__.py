import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def chats(): click.echo('LiveChat chats')
@cli.command()
def agents(): click.echo('LiveChat agents')
if __name__ == '__main__': cli()
