import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('phpbb running')
@cli.command()
def start(): click.echo('phpbb started')
if __name__ == '__main__': cli()
