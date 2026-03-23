import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('lua running')
@cli.command()
def start(): click.echo('lua started')
if __name__ == '__main__': cli()
