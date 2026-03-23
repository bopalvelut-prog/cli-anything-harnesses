import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('recover running')
@cli.command()
def start(): click.echo('recover started')
if __name__ == '__main__': cli()
