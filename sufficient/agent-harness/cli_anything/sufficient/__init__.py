import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('sufficient running')
@cli.command()
def start(): click.echo('sufficient started')
if __name__ == '__main__': cli()
