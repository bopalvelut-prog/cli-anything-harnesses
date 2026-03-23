import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('derby running')
@cli.command()
def start(): click.echo('derby started')
if __name__ == '__main__': cli()
