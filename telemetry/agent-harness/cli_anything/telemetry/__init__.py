import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('telemetry running')
@cli.command()
def start(): click.echo('telemetry started')
if __name__ == '__main__': cli()
