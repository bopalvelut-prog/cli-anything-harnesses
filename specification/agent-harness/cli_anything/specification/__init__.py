import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('specification running')
@cli.command()
def start(): click.echo('specification started')
if __name__ == '__main__': cli()
