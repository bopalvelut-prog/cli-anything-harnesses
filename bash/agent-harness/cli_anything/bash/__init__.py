import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('bash running')
@cli.command()
def start(): click.echo('bash started')
if __name__ == '__main__': cli()
