import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('tuning running')
@cli.command()
def start(): click.echo('tuning started')
if __name__ == '__main__': cli()
