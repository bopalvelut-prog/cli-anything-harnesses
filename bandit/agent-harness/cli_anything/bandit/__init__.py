import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('bandit running')
@cli.command()
def start(): click.echo('bandit started')
if __name__ == '__main__': cli()
