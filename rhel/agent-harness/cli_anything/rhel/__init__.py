import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('rhel running')
@cli.command()
def start(): click.echo('rhel started')
if __name__ == '__main__': cli()
