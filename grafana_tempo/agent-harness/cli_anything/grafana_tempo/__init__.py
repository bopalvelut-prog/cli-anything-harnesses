import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('grafana_tempo running')
@cli.command()
def start(): click.echo('grafana_tempo started')
if __name__ == '__main__': cli()
