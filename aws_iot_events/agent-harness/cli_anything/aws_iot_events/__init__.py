import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('aws_iot_events running')
@cli.command()
def start(): click.echo('aws_iot_events started')
if __name__ == '__main__': cli()
