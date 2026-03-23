import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('yugabyte running')
@cli.command()
def start(): click.echo('yugabyte started')
if __name__ == '__main__': cli()
