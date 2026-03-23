import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('procstat running')
@cli.command()
def start(): click.echo('procstat started')
if __name__ == '__main__': cli()
