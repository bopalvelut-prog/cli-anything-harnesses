import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('behat running')
@cli.command()
def start(): click.echo('behat started')
if __name__ == '__main__': cli()
