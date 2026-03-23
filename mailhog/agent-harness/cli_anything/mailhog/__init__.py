import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('mailhog running')
@cli.command()
def start(): click.echo('mailhog started')
if __name__ == '__main__': cli()
