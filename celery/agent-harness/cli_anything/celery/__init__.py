import click, subprocess
@click.group()
def cli(): pass
@cli.command()
@click.option('--broker', default='amqp://')
def worker(broker): subprocess.run(['celery', '-A', 'app', 'worker', '--broker', broker])
@cli.command()
def tasks(): click.echo('Celery tasks')
@cli.command()
def status(): subprocess.run(['celery', '-A', 'app', 'inspect', 'active'])
if __name__ == '__main__': cli()
