import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('smooth running')
@cli.command()
def start(): click.echo('smooth started')
if __name__ == '__main__': cli()
