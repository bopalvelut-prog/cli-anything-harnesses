import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('teacher running')
@cli.command()
def start(): click.echo('teacher started')
if __name__ == '__main__': cli()
