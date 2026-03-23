import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('aws_service_quotas running')
@cli.command()
def start(): click.echo('aws_service_quotas started')
if __name__ == '__main__': cli()
