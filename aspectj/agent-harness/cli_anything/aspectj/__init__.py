import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('aspectj running')
@cli.command()
def start(): click.echo('aspectj started')
if __name__ == '__main__': cli()
