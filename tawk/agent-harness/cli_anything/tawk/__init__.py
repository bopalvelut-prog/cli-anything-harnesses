import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def chats(): click.echo('tawk.to chats')
@cli.command()
def agents(): click.echo('tawk.to agents')
if __name__ == '__main__': cli()
