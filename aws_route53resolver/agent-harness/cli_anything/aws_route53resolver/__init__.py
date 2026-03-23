import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('aws_route53resolver running')
@cli.command()
def start(): click.echo('aws_route53resolver started')
if __name__ == '__main__': cli()
